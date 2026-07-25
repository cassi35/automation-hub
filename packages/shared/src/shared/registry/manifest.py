class AutomationManifest:
    def __init__(self, slug, name, description, trigger_type, schedule=None):
        self.slug = slug
        self.name = name
        self.description = description
        self.trigger_type = trigger_type
        self.schedule = schedule