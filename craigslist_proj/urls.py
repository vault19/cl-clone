"""craigslist_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from cl_app.views import IndexView, RegisterView, SearchListView, ListingUpdateView, ListingDeleteView, ListingTypeCreateView, ListingCreateView, ListingDetailView, ProfileView, CityListView, CategoryListView, CityCategoryListView
from cl_api.views import ListingListCreateAPIView, ListingRetrieveUpdateAPIView, CategoryListCreateAPIView, CategoryRetriveUpdateAPIView, SubCategoryListCreateAPIView, SubCategoryRetriveUpdateAPIView, CategoryListingListAPIView, SubCategoryListingListAPIView, UserCreateAPIView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index_view'),
    path('register/', RegisterView.as_view(), name='register_view'),
    path('register/profile/', ProfileView.as_view(), name='profile_view'),
    path('search/', SearchListView.as_view(), name='search_list_view'),
    path('listingcreate/<str:category_slug>/', ListingCreateView.as_view(), name='listing_create_view'),
    path('listingupdate/<uuid:pk>/', ListingUpdateView.as_view(), name='listing_update_view'),
    path('listingdelete/<uuid:pk>/', ListingDeleteView.as_view(), name='listing_delete_view'),
    path('listing/<uuid:pk>/', ListingDetailView.as_view(), name='listing_detail_view'),
    path('catergory/<int:category_id>/', CategoryListView.as_view(), name='category_list_view'),
    path('city/<str:city_slug>/', CityListView.as_view(), name='city_list_view'),
    path('city/<str:city_slug>/<str:category_slug>/', CityCategoryListView.as_view(), name='city_category_list_view'),
    # path('about/', AboutView.as_view(), name='about_view'),
    # Start API urls
#    path('api/api-token-auth/', views.obtain_auth_token),
#    path('api/register/', UserCreateAPIView.as_view(), name='create_user_view'),
#    path('api/listings/', ListingListCreateAPIView.as_view(), name='listing-list'),
#    path('api/listings/(?P<pk>\d+)/', ListingRetrieveUpdateAPIView.as_view(), name='listing-detail'),

#    path('api/categories/', CategoryListCreateAPIView.as_view(), name='categories-list'),
#    path('api/categories/(?P<pk>\d+)/', CategoryRetriveUpdateAPIView.as_view(), name='categories-detail'),

#    path('api/sub_categories/', SubCategoryListCreateAPIView.as_view(), name='sub-categories-list'),
#    path('api/sub_categories/(?P<pk>\d+)/', SubCategoryRetriveUpdateAPIView.as_view(), name='sub-categories-detail'),

#    path('api/category_listings/(?P<pk>\d+)/', CategoryListingListAPIView.as_view(), name='category-listings-list'),
#    path('api/sub_category_listings/(?P<pk>\d+)/', SubCategoryListingListAPIView.as_view(), name='sub-category-listings-list'),
#    path('api/docs/', include('rest_framework_docs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path('i18n/', include('django.conf.urls.i18n')),]
urlpatterns += i18n_patterns(path('admin/', admin.site.urls))