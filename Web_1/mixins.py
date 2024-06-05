class DataMixin(object):
    def get_context_data(self, **kwargs):
        context = super()
        #context['staff'] = User.objects.filter(is_staff=True)
        return context
    def get_user_data(self, **kwargs):
        ...