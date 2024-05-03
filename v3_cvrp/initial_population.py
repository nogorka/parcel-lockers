from random import sample

from v2oop.objects.route import Route
from v3_cvrp.individual import Individual


def create_feasible_route(available_points, vehicle_capacity):
    route = []
    current_demand = 0
    shuffled_available_points = sample(available_points, len(available_points))

    not_suitable_points = []
    while current_demand < vehicle_capacity:
        if len(shuffled_available_points) > 0:
            point = shuffled_available_points.pop()
            if current_demand + point.demand <= vehicle_capacity:
                route.append(point)
                current_demand += point.demand
            else:
                not_suitable_points.append(point)
        else:
            break
    return Route(route), shuffled_available_points + not_suitable_points


def generate_initial_population(population_size, points, vehicle_capacity):
    population = []

    for i in range(population_size):
        remaining_points = points.copy()
        individual = Individual()

        while len(remaining_points) > 0:
            new_route, remaining_points = create_feasible_route(remaining_points, vehicle_capacity)
            if new_route and new_route.points:  # Ensure only non-empty routes are added
                individual.add_route(new_route)

        population.append(individual)

    return population

