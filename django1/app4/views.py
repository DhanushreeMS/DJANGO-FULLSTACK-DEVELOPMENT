from django.shortcuts import render
from .forms import WordInputForm
from itertools import permutations

def calculate_permutations(request):
    permutations_result = {}
    if request.method == 'POST':
        form = WordInputForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word'].upper() 
            
            def generate_permutations(word):
                if len(word) == 0:
                    return ['']

                perms = []
                for i in range(len(word)):
                    remaining_chars = word[:i] + word[i+1:]
                    for perm in generate_permutations(remaining_chars):
                        perms.append(word[i] + perm)
                return perms

            if len(word) in [3, 4, 5]:
                permutations_result[f'perm{len(word)}'] = generate_permutations(word)

    else:
        form = WordInputForm()

    return render(request, 'app4/index.html', {'form': form, 'permutations_result': permutations_result})
