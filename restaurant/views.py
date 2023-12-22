from django.shortcuts import render, redirect
from django.http import HttpResponse
from restaurant.models import *
from restaurant.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def user (request):
    users = User.objects.all()
    data = {
        'users': users,
       
    }
    return render(request, 'user/user.html', data)

def tambah_user(request):
    if request.POST:
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            form = FormUser()
            pesan = 'Data berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan
            }
            return render(request, 'user/tambah-user.html', konteks)
    else:         
        konteks = {
            'form': FormUser()
        }
        return render(request, 'user/tambah-user.html', konteks)

def ubah_user(request, id_user):
    user = User.objects.get(id=id_user)
    template= 'user/ubah-user.html'
    
    if request.POST:
        form = FormUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('user/ubah_user', id_user=id_user)
    else:
        form = FormUser(instance=user)
        konteks = {
            'form': form,
            'user': user
        }
    return render(request, template, konteks)
            
def hapus_user(request, id_user):
    user = User.objects.filter(id=id_user)
    user.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect('user')
   
# table   
def table (request):
    tables = Table.objects.all()
    data = {
        'tables': tables,
       
    }
    return render(request, 'table/table.html', data)

def tambah_table(request):
    if request.POST:
        form = FormTable(request.POST)
        if form.is_valid():
            form.save()
            form = FormTable()
            pesan = 'Data berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan
            }
            return render(request, 'table/tambah-table.html', konteks)
    else:         
        konteks = {
            'form': FormTable()
        }
        return render(request, 'table/tambah-table.html', konteks)

def ubah_table(request, id_table):
    table = Table.objects.get(id=id_table)
    template= 'table/ubah-table.html'
    
    if request.POST:
        form = FormTable(request.POST, instance=table)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_table', id_table=id_table)
    else:
        form = FormTable(instance=table)
        konteks = {
            'form': form,
            'table': table
        }
    return render(request, template, konteks)
            
def hapus_table(request, id_table):
    table = Table.objects.filter(id=id_table)
    table.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect('table')
   

# menu   
def menu (request):
    menus = Menu.objects.all()
    data = {
        'menus': menus,
       
    }
    return render(request, 'menu/menu.html', data)

def tambah_menu(request):
    if request.POST:
        form = FormMenu(request.POST)
        if form.is_valid():
            form.save()
            form = FormMenu()
            pesan = 'Data berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan
            }
            return render(request, 'menu/tambah-menu.html', konteks)
    else:         
        konteks = {
            'form': FormMenu()
        }
        return render(request, 'menu/tambah-menu.html', konteks)

def ubah_menu(request, id_menu):
    menu = Menu.objects.get(id=id_menu)
    template= 'menu/ubah-menu.html'
    
    if request.POST:
        form = FormMenu(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_menu', id_menu=id_menu)
    else:
        form = FormMenu(instance=menu)
        konteks = {
            'form': form,
            'menu': menu
        }
    return render(request, template, konteks)
            
def hapus_menu(request, id_menu):
    menu = Menu.objects.filter(id=id_menu)
    menu.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect('menu')
   
   
# formula   
def formula (request):
    formulas = Formula.objects.all()
    data = {
        'formulas': formulas,
       
    }
    return render(request, 'formula/formula.html', data)

def tambah_formula(request):
    if request.POST:
        form = FormFormula(request.POST)
        if form.is_valid():
            form.save()
            form = FormFormula()
            pesan = 'Data berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan
            }
            return render(request, 'formula/tambah-formula.html', konteks)
    else:         
        konteks = {
            'form': FormFormula()
        }
        return render(request, 'formula/tambah-formula.html', konteks)

def ubah_formula(request, id_formula):
    formula = Formula.objects.get(id=id_formula)
    template= 'formula/ubah-formula.html'
    
    if request.POST:
        form = FormFormula(request.POST, instance=formula)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_formula', id_formula=id_formula)
    else:
        form = FormFormula(instance=formula)
        konteks = {
            'form': form,
            'formula': formula
        }
    return render(request, template, konteks)
            
def hapus_formula(request, id_formula):
    formula = Formula.objects.filter(id=id_formula)
    formula.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect('formula')


# order   
def order (request):
    orders = Order.objects.all()
    data = {
        'orders': orders,
       
    }
    return render(request, 'order/order.html', data)

def tambah_order(request):
    if request.POST:
        form = FormOrder(request.POST)
        if form.is_valid():
            form.save()
            form = FormOrder()
            pesan = 'Data berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan
            }
            return render(request, 'order/tambah-order.html', konteks)
    else:         
        konteks = {
            'form': FormOrder()
        }
        return render(request, 'order/tambah-order.html', konteks)

def ubah_order(request, id_order):
    order = Order.objects.get(id=id_order)
    template= 'ubah-order.html'
    
    if request.POST:
        form = FormOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_order', id_order=id_order)
    else:
        form = FormOrder(instance=table)
        konteks = {
            'form': form,
            'order': order
        }
    return render(request, template, konteks)
            
def hapus_order(request, id_order):
    order = Order.objects.filter(id=id_order)
    order.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect('order')
      