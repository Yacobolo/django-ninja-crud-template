from http import HTTPStatus
from typing import Callable, List, Optional, Type

from django.db.models import Model
from django.http import HttpRequest
from ninja import Router
from ninja_crud.views import utils
from ninja_crud.views.abstract import AbstractModelView
from ninja_crud.views.types import PostDeleteHook, PreDeleteHook


class SoftDeleteModelView(AbstractModelView):
    def __init__(
        self,
        pre_delete: PreDeleteHook = None,
        post_delete: PostDeleteHook = None,
        decorators: List[Callable] = None,
        router_kwargs: Optional[dict] = None,
    ) -> None:
        super().__init__(decorators=decorators, router_kwargs=router_kwargs)
        self.pre_delete = pre_delete
        self.post_delete = post_delete

    def register_route(self, router: Router, model_class: Type[Model]) -> None:
        @router.delete(**self._get_default_router_kwargs(model_class))
        @utils.merge_decorators(self.decorators)
        def delete_model(request: HttpRequest, id: utils.get_id_type(model_class)):
            instance = model_class.objects.get(pk=id)

            if self.pre_delete is not None:
                self.pre_delete(request, instance)

            instance.is_deleted = True
            instance.save()

            if self.post_delete is not None:
                self.post_delete(request, id, instance)

            return HTTPStatus.NO_CONTENT, None

    def _get_default_router_kwargs(self, model_class: Type[Model]) -> dict:
        return dict(
            path=self.get_path(),
            response={HTTPStatus.NO_CONTENT: None},
            operation_id=self._get_operation_id(model_class),
            summary=self._get_summary(model_class),
        )

    def get_path(self) -> str:
        return "/{id}"

    @staticmethod
    def _get_operation_id(model_class: Type[Model]) -> str:
        return f"delete_{utils.to_snake_case(model_class.__name__)}"

    @staticmethod
    def _get_summary(model_class: Type[Model]) -> str:
        return f"Delete {model_class.__name__}"
