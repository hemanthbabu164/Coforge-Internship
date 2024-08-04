from django.urls import path 
from .views import DocumentUploadView, DocumentPreprocessView, SummaryQueryView

urlpatterns=[
    path('upload/', DocumentUploadView.as_view(), name='upload_document'),
    path('preprocess/', DocumentPreprocessView.as_view(), name='preprocess_document'),
    path('summary/', SummaryQueryView.as_view(), name='summary_query'),
]