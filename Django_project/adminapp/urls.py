from django.urls import path
import adminapp.views as adminapp


app_name = "adminapp"

urlpatterns = [
    # path('', adminapp.index, name='index'),
    path("", adminapp.UserList.as_view(), name="index"),
    path("user/create/", adminapp.user_create, name="user_create"),
    path("user/<int:pk>/update/", adminapp.user_update, name="user_update"),
    path("user/<int:pk>/delete/", adminapp.user_delete, name="user_delete"),
    # path('categories/read/', adminapp.categories_read, name='categories_read'),
    path(
        "categories/read/",
        adminapp.ProductCategoriesRead.as_view(),
        name="categories_read",
    ),
    path(
        "category/create/",
        adminapp.ProductCategoryCreate.as_view(),
        name="category_create",
    ),
    path(
        "category/<int:category_pk>/update/",
        adminapp.ProductCategoryUpdate.as_view(),
        name="category_update",
    ),
    path(
        "category/<int:pk>/delete/",
        adminapp.ProductCategoryDelete.as_view(),
        name="category_delete",
    ),
    path(
        "category/<int:category_pk>/products/",
        adminapp.category_products,
        name="category_products",
    ),
    path(
        "category/<int:category_pk>/product/create/",
        adminapp.product_create,
        name="product_create",
    ),
    path(
        "product/<int:product_pk>/read/",
        adminapp.ProductDetail.as_view(),
        name="product_read",
    ),
    path("product/<int:pk>/update/", adminapp.product_update, name="product_update"),
    path("product/<int:pk>/delete/", adminapp.product_delete, name="product_delete"),
]
