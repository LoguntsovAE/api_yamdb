from rest_framework import mixins, viewsets


class CreateDestroyReadOnlyCustom(mixins.CreateModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.ListModelMixin,
                                  viewsets.GenericViewSet):
    pass
