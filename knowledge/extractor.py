class InformationExtractor:
    """
    Converts raw research information into
    structured information that Caine can understand.

    This layer allows future replacement with:
    - AI models
    - NLP systems
    - external analysis tools
    """



    def extract(
        self,
        information
    ):


        if information is None:

            return None



        if isinstance(
            information,
            dict
        ):

            return information



        if isinstance(
            information,
            str
        ):

            return self.extract_from_text(
                information
            )



        return None





    def extract_from_text(
        self,
        text
    ):


        text_lower = text.lower()



        result = {


            "name":
            "",


            "category":
            "unknown",


            "features":
            [],


            "materials":
            [],


            "systems":
            [],


            "relationships":
            []

        }



        # Feature detection

        feature_words = [

            "tower",
            "towers",
            "wall",
            "walls",
            "room",
            "rooms",
            "floating",
            "flying",
            "magical",
            "magic"

        ]



        for word in feature_words:


            if word in text_lower:


                result["features"].append(
                    word
                )



        # Materials

        material_words = [

            "stone",
            "wood",
            "metal",
            "crystal",
            "glass"

        ]



        for word in material_words:


            if word in text_lower:


                result["materials"].append(
                    word
                )



        # Systems

        system_words = [

            "energy",
            "magic",
            "levitation",
            "technology"

        ]



        for word in system_words:


            if word in text_lower:


                result["systems"].append(
                    word
                )



        return result