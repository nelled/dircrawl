def prepare_url(url):
    if url[-1] != '/':
        return url + '/'
    else:
        return url


def read_word_list(word_list_path):
    result = []
    with open(word_list_path, 'r') as file:
        for line in file:
            l = line.strip()
            if not l.startswith('#'):
                result.append(l)
    return result
