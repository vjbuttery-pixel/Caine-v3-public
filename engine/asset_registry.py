from datetime import datetime


class AssetRegistry:
    """
    Stores information about every asset
    created by Caine.

    This acts as Caine's asset memory,
    preventing duplicate creation and
    tracking dependencies.
    """

    def __init__(self):

        self.assets = {}

        self.history = []



    def register_asset(
        self,
        name,
        asset_type,
        location,
        creator
    ):

        asset_id = (
            f"{asset_type}_{len(self.assets)+1}"
        )


        asset = {

            "id": asset_id,

            "name": name,

            "type": asset_type,

            "location": location,

            "creator": creator,

            "created":
                datetime.utcnow()
                .isoformat(),

            "versions": [

                "1.0"

            ],

            "dependencies": []

        }


        self.assets[asset_id] = asset


        self.history.append({

            "event":
                "asset_created",

            "asset":
                asset_id

        })


        return asset



    def find_asset(
        self,
        name
    ):

        for asset in self.assets.values():

            if asset["name"] == name:

                return asset


        return None



    def add_dependency(
        self,
        asset_id,
        dependency
    ):

        if asset_id in self.assets:

            self.assets[asset_id][
                "dependencies"
            ].append(dependency)



    def create_version(
        self,
        asset_id
    ):

        if asset_id not in self.assets:

            return None


        versions = (
            self.assets[asset_id]
            ["versions"]
        )


        version_number = len(
            versions
        ) + 1


        new_version = (
            f"1.{version_number-1}"
        )


        versions.append(
            new_version
        )


        return new_version



    def remove_asset(
        self,
        asset_id
    ):

        if asset_id in self.assets:

            del self.assets[asset_id]


            self.history.append({

                "event":
                    "asset_removed",

                "asset":
                    asset_id

            })


            return True


        return False



    def get_project_assets(
        self,
        asset_type=None
    ):

        results = []


        for asset in self.assets.values():

            if asset_type is None:

                results.append(asset)

            elif asset["type"] == asset_type:

                results.append(asset)


        return results



    def summary(self):

        return {

            "total_assets":
                len(self.assets),

            "history_events":
                len(self.history)

        }