
# %%

from doctest import master


yoda = {
    'age': 910,
    'species': 'Yodas',
    'gender': 'male',
    'affiliations': ['Jodi', 'Galactic Republic'],
    'master': {
        'name': 'Qui-Gon Jinn',
        'age': 48,
        'affiliations': ['jodi', 'Galactic Republic', 'Heliost Clan'],
        'master': {
            'name': 'Dooku',
            'age': 83,
            'affiliations': ['House serenno', 'Jodi']
        }
    }
}

print(yoda['master']['master']['name'])
yoda['master']['master']['affiliations'].append('Sith')
print(yoda['master']['master']['affiliations'])
yoda.pop('master')
print(yoda)