from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import APIException
from .scripts.doc_summarizer import preprocess_document
import os
import json

# Create your views here.
class DocumentUploadView(APIView):
    parser_classes= (MultiPartParser,FormParser)
    
    def post(self,request,*args,**kwargs):
        file=request.FILES.get('file')
        if not file:
            return JsonResponse({'error':'No FILE Provided'}, status=400)
        print(f"Uploaded file name: {file.name}")
        try:
            with open('uploads/uploaded_file.pdf' , 'wb+') as localfile:
                for chunk in file.chunks():
                    localfile.write(chunk)
        except Exception as e:
            return JsonResponse({'error' : f'Error Saving the File:{str(e)}'},status=500)
        
        return JsonResponse({'message':"File Uploaded Successfully."},status=200)

class DocumentPreprocessView(APIView):
    def post(self,request,*args,**kwargs):
        file_path='uploads/uploaded_file.pdf'
        if not os.path.exists(file_path):
            return JsonResponse({'error':"No File Found to Preprocess"},status=400)
        output_path='uploads/summary_output.json'
        try:
            key_value_pairs=preprocess_document(file_path)
            with open(output_path,'w') as output_file:
                json.dump(key_value_pairs,output_file, indent=4)
            return JsonResponse({'message':"Document Preprocessed Successfully.0"},status=200)
        except Exception as e:
            return JsonResponse({'error':f'Error During Preprocessing:{str(e)}'},status=500)
        return JsonResponse({'message': "File Preprocessed Successfully."},status=200)

class SummaryQueryView(APIView):
    def get(self,request,*args,**kwargs):
        keyword=request.query_params.get('keyword','').strip().lower()
        if not keyword:
            return JsonResponse({'error': "No Keyword Entered."}, status=400)
        output_path='uploads/summary_output.json'
        if not os.path.exists(output_path):
            return JsonResponse({'error':"No Sumamry File Found "},status=400)
        
        try:
            with open(output_path,'r') as output_file:
                summaries=json.load(output_file)
            print(summaries)
            result = {sentence: data["summary"] for sentence, data in summaries.items() if any(keyword in k.lower() for k in data["keywords"])}
            if not result:
                return JsonResponse({'message':"No Summary Found for the give Keyword"},status=404)
            return JsonResponse(result,safe=False,status=200)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=500) 