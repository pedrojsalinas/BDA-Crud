from django.shortcuts import render, get_object_or_404,redirect
from django.template import loader
from django.views.generic import TemplateView
from proyecto.models import *
from proyecto.forms import *

class VictimaView(TemplateView):
    template_name = 'proyecto/victimas.html'
    def get(self,request):
        form = VictimaForm()
        victimas = Victima.objects.all()
        return render(request, self.template_name ,{'victimas': victimas, 'form':form})
    def post(self, request):
        form = VictimaForm(request.POST)
        if form.is_valid():
            form.save()
            form = VictimaForm
        victimas = Victima.objects.all()
        args = {'victimas': victimas,'form':form}
        return render(request, self.template_name , args)

class AgresorView(TemplateView):
    template_name = 'proyecto/agresores.html'
    def get(self,request):
        form = AgresorForm()
        agresores = Agresor.objects.all()
        return render(request, self.template_name ,{'agresores': agresores,'form':form})

    def post(self, request):
        form = AgresorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AgresorForm
        agresores = Agresor.objects.all()
        args = {'agresores': agresores,'form':form}
        return render(request, self.template_name , args)

class FemicidioView(TemplateView):
    template_name = 'proyecto/femicidios.html'
    def get(self,request):
        form = FemicidioForm()
        femicidios = Femicidio.objects.all()
        return render(request, self.template_name ,{'femicidios': femicidios, 'form':form})
    def post(self, request):
        form = FemicidioForm(request.POST)
        if form.is_valid():
            form.save()
            form = FemicidioForm
        femicidios = Femicidio.objects.all()
        args = {'femicidios': femicidios,'form':form}
        return render(request, self.template_name , args)

class AgresorDetalleView(TemplateView):
    template_name = 'proyecto/detalle-agresor.html'
    def get(self,request, id):
        agresor = Agresor.objects.get(pk=id)
        form = AgresorForm(instance=agresor)
        args = {'agresor': agresor,'form':form}
        return render(request, self.template_name , args)
    def post(self, request, id):
        instance = get_object_or_404(Agresor, id=id)
        form = AgresorForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('agresores')
        args = {'form':form}
        return render(request, self.template_name , args)
    def eliminar(request,pk):
        agresor = get_object_or_404(Agresor, pk=pk)
        agresor.delete()
        return redirect('agresores')

class VictimaDetalleView(TemplateView):
    template_name = 'proyecto/detalle-victima.html'
    def get(self,request, id):
        victima = Victima.objects.get(pk=id)
        form = VictimaForm(instance=victima)
        args = {'victima': victima,'form':form}
        return render(request, self.template_name , args)
    def post(self, request, id):
        instance = get_object_or_404(Victima, id=id)
        form = VictimaForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('victimas')
        args = {'form':form}
        return render(request, self.template_name , args)
    def eliminar(request,pk):
        victima = get_object_or_404(Victima, pk=pk)
        victima.delete()
        return redirect('victimas')

class FemicidioDetalleView(TemplateView):
    template_name = 'proyecto/detalle-femicidio.html'
    def get(self,request, id):
        femicidio = Femicidio.objects.get(pk=id)
        form = FemicidioForm(instance=femicidio)
        args = {'femicidio': femicidio,'form':form}
        return render(request, self.template_name , args)
    def post(self, request, id):
        instance = get_object_or_404(Femicidio, id=id)
        form = FemicidioForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('femicidios')
        args = {'form':form}
        return render(request, self.template_name , args)
    def eliminar(request,pk):
        femicidio = get_object_or_404(Femicidio, pk=pk)
        femicidio.delete()
        return redirect('femicidios')

class RelacionView(TemplateView):
    template_name = 'proyecto/relaciones.html'
    def get(self,request):
        relaciones = Relacion.objects.all()
        return render(request, self.template_name ,{'relaciones': relaciones})
