from django.urls import path
from .views import StudentRecordFormView, StudentCreateView, FormSuccessView, StudentRecordDetailView, StudentRecordUpdate, StudentRecordDelete

urlpatterns = [
    path('new_student_record', StudentRecordFormView.as_view(), name='student_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('create_new_student_record', StudentCreateView.as_view(), name='c_student_record_form'),
    path('student_record_detail/<int:pk>', StudentRecordDetailView.as_view(), name='r_student_record'),
    path('student_record_update/<int:pk>', StudentRecordUpdate.as_view(), name='u_student_record'),
    path('student_record_delete/<int:pk>', StudentRecordDelete.as_view(), name='d_student_record')
]