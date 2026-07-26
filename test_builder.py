from brain.caine import Caine



def run_test():

    print("==============================")
    print(" CAINE V3 SYSTEM TEST")
    print("==============================\n")


    caine = Caine()


    idea = (
        "a magical flying castle above a candy forest"
    )


    print("INPUT IDEA:")
    print(idea)


    print("\n==============================")
    print("RUNNING CAINE...")
    print("==============================\n")


    result = caine.create(
        idea
    )


    print("\n==============================")
    print("FINAL OUTPUT")
    print("==============================\n")


    print(
        result.describe()
    )



if __name__ == "__main__":

    run_test()