def auto_info(company, model, colour, gearboxes, year, cost=None):
    auto = {
        'company': company,
        'model': model,
        'colour': colour,
        'gearboxes': gearboxes,
        'year': year,
        'cost': cost
    }

    return auto


def enter_auto():
    print("We'll make a list of cars in our website.")
    autos = []
    while True:
        print("\nEnter below info:")
        company = input("Producer of the car: ")
        model = input("Model of the car: ")
        colour = input("Colour of the car: ")
        gearboxes = input("Transmission of the car: ")
        year = input("Produced year: ")
        cost = input("Cost of the car: ")

        autos.append(auto_info(company, model, colour, gearboxes, year, cost))

        prompt = input("Will you add more cars? (yes/no)")
        if prompt == 'no':
            break

def info_print(auto_info):
    print("Cars in the Salon")
    print(f"{auto_info['colour'].title()} {auto_info['company'].title()} {auto_info['model'].title()}, {auto_info['gearboxes']}, {auto_info['year']}-year, costs: {auto_info['cost']}$")
