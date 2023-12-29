def groupPath(argMajors, argYears, majors, years):
    years_dict = {
        years[0]: "1",
        years[1]: "2",
        years[2]: "3",
        years[3]: "4",
        years[4]: "5",
    }

    majors_dict = {
        majors[0]: "AI",
        majors[1]: "CS",
        majors[2]: "B",
        majors[3]: "BT",
        majors[4]: "ENG",
    }
    return str(majors_dict.get(argMajors)) + \
    str(years_dict.get(argYears))