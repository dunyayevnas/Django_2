from django.shortcuts import render, HttpResponse


from .models import Pupil


# Create your views here.
def pupils_list(request):
    if 'pupil' not in request.GET:
        pupils = Pupil.objects.all() # SELECT * FROM pupils;
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})
    else:
        pupils = Pupil.objects.filter(name__icontains=request.GET['pupil'])
        # SELECT * FROM pupils WHERE name LIKE '%str%';
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})


def pupils_detail(request, pk):
    pupil = Pupil.objects.get(id=pk)
    return render(request, 'pupils/pupil_info.html', {'pupil': pupil})




def delete_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        # Здесь можно добавить код для удаления продукта из базы данных или другого источника данных
        return HttpResponse(f"Продукт {product_name} успешно удален.")
    else:
        return render(request, 'pupil_info.html/pupils_list.html')
