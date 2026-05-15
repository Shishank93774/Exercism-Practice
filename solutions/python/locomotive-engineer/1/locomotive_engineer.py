"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
       An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]) The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    each_wagons_id = each_wagons_id[2:] + each_wagons_id[:2]
    try:
        idx = each_wagons_id.index(1)
    except ValueError as ve:
        idx = len(each_wagons_id) - 1
    except Exception as e:
        return

    each_wagons_id = each_wagons_id[:idx+1] + missing_wagons + each_wagons_id[idx+1:]
    return each_wagons_id


def add_missing_stops(route, **stops_dict):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    route['stops'] = list(stops_dict.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    route = {**route, **more_route_information}

    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[tuple]) The list of rows of wagons.

    Returns:
        list[tuple]: the list of rows of wagons.
    """
    return [[x, y, z] for x, y, z, in zip(wagons_rows[0], wagons_rows[1], wagons_rows[2])]