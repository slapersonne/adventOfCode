import functools
import re


def parse_passport(passport_content):
    return {key: value for key, value in (field.split(":") for field in passport_content)}


def parse_passports(lines):
    split_indexes = [i for i, val in enumerate(lines) if val == ""]
    passports = [
        parse_passport(functools.reduce(list.__add__, shards)) for shards in
        (map(lambda shard: shard.split(" "), content) for content in
        (lines[i+1:j] for i, j in zip([-1] + split_indexes, split_indexes + [len(lines)])))
    ]
    return passports


def validate(passport, validate_values=True):
    required_fields = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    if not set(required_fields).issubset(set(passport.keys())):
        return False
    else:
        return not validate_values or validate_fields(passport)


def validate_fields(fields):
    birth_year = int(fields["byr"])
    if not 1920 <= birth_year <= 2002:
        return False

    issue_year = int(fields["iyr"])
    if not 2010 <= issue_year <= 2020:
        return False

    expiration_year = int(fields["eyr"])
    if not 2020 <= expiration_year <= 2030:
        return False

    height = fields["hgt"]
    hgt_rgxp = r"(\d+)(cm|in)"
    hgt_match = re.match(hgt_rgxp, height)
    if not hgt_match:
        return False
    else:
        n, unit = int(hgt_match.group(1)), hgt_match.group(2)
        if unit not in ["in", "cm"]:
            return False
        elif unit == "in" and not 59 <= n <= 76:
            return False
        elif unit == "cm" and not 150 <= n <= 193:
            return False

    hair_color = fields["hcl"]
    if not re.match(r"#[\da-f]{6}", hair_color):
        return False

    eye_color = fields["ecl"]
    if not eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    passport_id = fields["pid"]
    if not re.match(r"\d{9}", passport_id):
        return False

    return True


def run_04():
    with open("inputs/d04.txt") as f:
        lines = [line[:-1] for line in f.readlines()]
    passports = parse_passports(lines)
    valid_passports = [passport for passport in passports if validate(passport, True)]
    print(len(valid_passports))
    return
