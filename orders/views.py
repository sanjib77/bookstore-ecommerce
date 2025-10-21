# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import Order, OrderItem
from cart.models import Cart

@login_required
def create_order(request):
    """Create order from cart"""
    cart = get_object_or_404(Cart, user=request.user)
    
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:view_cart')
    
    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            order_number=get_random_string(10).upper(),
            total_amount=cart.total_price,
            shipping_address=request.POST.get('address'),
            shipping_city=request.POST.get('city'),
            shipping_state=request.POST.get('state'),
            shipping_zip=request.POST.get('zip'),
            shipping_country=request.POST.get('country'),
        )
        
        # Create order items from cart
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                book=cart_item.book,
                quantity=cart_item.quantity,
                price=cart_item.book.price
            )
            
            # Update stock
            book = cart_item.book
            book.stock_quantity -= cart_item.quantity
            book.save()
        
        # Clear cart
        cart.items.all().delete()
        
        messages.success(request, f'Order {order.order_number} placed successfully!')
        return redirect('orders:order_detail', order_id=order.id)
    
    return render(request, 'orders/checkout.html', {'cart': cart})

@login_required
def order_detail(request, order_id):
    """Display order details"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_list(request):
    """Display user's orders"""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})