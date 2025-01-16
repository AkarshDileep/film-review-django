from django import template

register = template.Library()

def chunks(content, chunk_size):
    chunk = []
    i = 0
    for data in content:
        chunk.append(data)
        i = i + 1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk = []
    yield chunk

register.filter('chunks', chunks)
