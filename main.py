import re

def match_alpha_only(s: str) -> bool:
    """
    Match strings that contain only alphabetic characters (uppercase or lowercase).
    """
    return re.match(r'^[a-zA-Z]+$', s) is not None

def match_all_lowercase(s: str) -> bool:
    """
    Match strings that contain only lowercase letters.
    """
    return re.match(r'^[a-z]+$', s) is not None

def match_all_uppercase(s: str) -> bool:
    """
    Match strings that contain only uppercase letters.s
    """
    return re.match(r'^[A-Z]+$', s) is not None

def match_email_format(s: str) -> bool:
    """
    Match a valid email address format (e.g., example@domain.com).
    """
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', s) is not None

def match_us_phone(s: str) -> bool:
    """
    Match a US phone number format: 123-456-7890
    """
    return re.match(r'^\d{3}-\d{3}-\d{4}$', s) is not None

def match_date_mmddyyyy(s: str) -> bool:
    """
    Match a date in the format MM/DD/YYYY.
    """
    return re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$', s) is not None

def match_postal_code(s: str) -> bool:
    """
    Match a 5-digit US ZIP code.
    """
    return re.match(r'^\d{5}$', s) is not None

def match_hex_color(s: str) -> bool:
    """
    Match a hex color code (e.g., #FFF or #FFFFFF).
    """
    return re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', s) is not None

def match_time_24h(s: str) -> bool:
    """
    Match a time in 24-hour format (e.g., 14:30).
    """
    return re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', s) is not None

def match_valid_username(s: str) -> bool:
    """
    Match a username that contains only letters, numbers, and underscores, and is 3–16 characters long.
    """
    return re.match(r'^[a-zA-Z0-9_]{3,16}$', s) is not None

def match_url(s: str) -> bool:
    """
    Match a simple HTTP or HTTPS URL.
    """
    return re.match(r'^(https?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d+)?(/.*)?$', s) is not None

def match_credit_card(s: str) -> bool:
    """
    Match a credit card number format: 4 groups of 4 digits separated by spaces or hyphens.
    Example: 1234-5678-9012-3456 or 1234 5678 9012 3456
    """
    # Pattern breakdown:
    # \d{4}         -> 4 digits
    # [ -]          -> followed by either a space or a hyphen
    # {3}           -> repeat that sequence 3 times
    # \d{4}         -> end with exactly 4 digits
    pattern = r'^\d{4}([ -])\d{4}\1\d{4}\1\d{4}$'
    
    return re.match(pattern, s) is not None

def match_hashtag(s: str) -> bool:
    """
    Match a valid hashtag that begins with # and is followed by alphanumeric characters.
    """
    return re.match(r'^#[a-zA-Z0-9]+$', s) is not None

def match_ip_address(s: str) -> bool:
    """
    Match a valid IPv4 address.
    """
    return re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', s) is not None

def match_strong_password(s: str) -> bool:
    """
    Match a strong password (at least 8 characters, one uppercase, one lowercase, one digit, and one special character).
    """
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', s) is not None


