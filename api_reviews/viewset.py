from rest_framework import mixins, viewsets


class CreateDesctroyReadOnlyCustom(mixins.CreateModelMixin,
                                   mixins.DestroyModelMixin,
                                   mixins.ListModelMixin,
                                   viewsets.GenericViewSet):
    pass
