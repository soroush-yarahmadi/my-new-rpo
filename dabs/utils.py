from accounts.serializers import AccountSer

class Utils:
    @staticmethod
    def get_or_none(model, **kwargs):
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            return None    