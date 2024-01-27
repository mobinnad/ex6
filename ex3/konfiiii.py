def collect_unique_domains(input_count):
    unique_domains = set()
    for _ in range(input_count):
        user_input = input()
        if "@" in user_input:
            _, domain = user_input.split('@', 1)
            unique_domains.add(domain)
    return unique_domains

def display_sorted_domains(domains_set):
    sorted_domains = sorted(domains_set)
    for domain in sorted_domains:
        print(domain)



email_count = int(input())
unique_domains_set = collect_unique_domains(email_count)
display_sorted_domains(unique_domains_set)
