from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like, Notification
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# Create y our views here 
