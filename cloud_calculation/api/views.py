from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CalculationInputSerializer, CalculationResultSerializer

class CalculationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalculationInputSerializer(data=request.data)
        if serializer.is_valid():
            input_data = serializer.validated_data['input_data']
            # Example calculation (replace with your actual logic)
            result = input_data * 2
            result_serializer = CalculationResultSerializer({'result': result})
            return Response(result_serializer.data)
        return Response(serializer.errors, status=400)
