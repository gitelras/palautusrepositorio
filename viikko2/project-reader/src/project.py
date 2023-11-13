class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, lice, auto):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = lice
        self.author = auto

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors = self._stringify_dependencies(self.author).split(',')
        depes = self._stringify_dependencies(self.dependencies).split(',')
        dev_depes = self._stringify_dependencies(self.dev_dependencies).split(',')

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors:"
     
            f"\n- {authors[0]}"
            f"\n-{authors[1]}"

            f'\n\nDependencies:'
            f"\n- {depes[0]}"
            f"\n-{depes[1]}"
            f"\n-{depes[2]}"

            f'\n\nDevelopment dependencies:'
            f"\n- {dev_depes[0]}"
            f"\n-{dev_depes[1]}"
            f"\n-{dev_depes[2]}"
            f"\n-{dev_depes[3]}"


        )
