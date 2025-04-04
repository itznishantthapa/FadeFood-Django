from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import FoodSerializer ,FoodImageSerializer
from .models import food ,food_image
from .models import restaurant
from authentications.permissions import IsSeller ,IsCustomer

@api_view(['POST'])
@permission_classes([IsSeller])
def add_food(request):
        try:
 
            restaurant = request.user.restaurant     # Access Restaurant via reverse OneToOneField
            food_restaurant = restaurant.name
            food_location = f"{restaurant.street_address}, {restaurant.city}"
            food_name = request.data.get('food_name')
            food_price = request.data.get('food_price')
            is_vegetarian=request.data.get('is_vegetarian')=='true'
            images = request.FILES.getlist('images') 
 


            food_data = food.objects.create(
                 restaurant_name=restaurant,
                 food_name=food_name, 
                 food_price=food_price,
                 food_restaurant=food_restaurant,
                 food_location=food_location,
                 is_vegetarian=is_vegetarian
                )

            image_instances=[]
            for img in images:
                try:
                    image_instance=food_image.objects.create(food_itemforFK=food_data, image=img)
                    image_instances.append(image_instance)
                except Exception as e:
                    return Response({"msg": f"Error saving image {img.name}", "error": str(e)}, status=400)


            food_serializer = FoodSerializer(food_data)
            image_serializer = FoodImageSerializer(image_instances, many=True)
            return Response({"ofBackendData":food_serializer.data,"msg":f"Food Added Successfully In {restaurant.name}"}, status=200)

        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)
        

@api_view(['GET'])
@permission_classes([IsSeller])
def get_food(request):
    try:
        restaurant = request.user.restaurant  # Access Restaurant via reverse OneToOneField
        foods = restaurant.food.all()  # Fetch all food items for this restaurant
        serializer = FoodSerializer(foods, many=True)
        return Response({"ofBackendData": serializer.data}, status=200)
    except Exception as e:
        return Response({"msg": str(e)}, status=400)
    

@api_view(['GET'])
@permission_classes([IsCustomer])  # Allow customers to access
def get_food_by_restaurant(request):
    try:
        restaurant_id = request.query_params.get("restaurant_id")
        if not restaurant_id:
            return Response({"msg": "Restaurant ID is required"}, status=400)
        
        get_restaurant = restaurant.objects.get(id=restaurant_id)  # Get restaurant
        foods = get_restaurant.food.filter(is_available=True)  # Get available food
        
        serializer = FoodSerializer(foods, many=True)
        return Response({"ofBackendData": serializer.data}, status=200)
    except restaurant.DoesNotExist:
        return Response({"msg": "Restaurant not found"}, status=404)
    except Exception as e:
        return Response({"msg": str(e)}, status=400)


@api_view(['PUT'])
@permission_classes([IsSeller])
def edit_food(request):
    try:
        food_id = request.data.get('id')
        if not food_id:
            return Response({"msg": "Food ID is required"}, status=400)

        # Fetch the food item
        food_data = food.objects.get(id=food_id, restaurant_name=request.user.restaurant)
        

        # Update food details using serializer
        serializer = FoodSerializer(food_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"msg": serializer.errors}, status=400)
        print('-----------------here')
        # Handle new images
        images = request.FILES.getlist('images')
        print(len(images))
        # valid_uris = request.FILES.getlist('images')
        if images:
            food_images = food_data.foodimage.all()
            if len(images)==1:
                food_images.last().delete()
                for img in images:
                    food_image.objects.create(food_itemforFK=food_data, image=img)
            elif len(images)==2:
                food_images[1].delete()
                food_images.last().delete()
                for img in images:
                    food_image.objects.create(food_itemforFK=food_data, image=img)

            elif len(images)==3:
                food_images.delete()
                for img in images:
                    food_image.objects.create(food_itemforFK=food_data, image=img)


            


        # Serialize updated data
        updated_serializer = FoodSerializer(food_data)
        return Response({
            "ofBackendData": updated_serializer.data,
            "msg": f"Food Updated Successfully in {food_data.restaurant_name.name}"
        }, status=200)

    except food.DoesNotExist:
        return Response({"msg": "Food item not found or does not belong to your restaurant."}, status=404)
    except Exception as e:
        return Response({"msg": str(e)}, status=400)

@api_view(['DELETE'])
@permission_classes([IsSeller])
def delete_food(request):
        try:
            restaurant = request.user.restaurant  # Access Restaurant via reverse OneToOneField
            food_id = request.data.get('id')

            # Fetch Food item belonging to the restaurant
            food = restaurant.food.filter(id=food_id).first()
            food.delete()
            return Response({"msg":"Food Deleted Successfully"}, status=200)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)
        

@api_view(['GET'])
@permission_classes([IsCustomer])
def get_all_food(request):
        try:
            foods = food.objects.all()
            serializer = FoodSerializer(foods, many=True)
            return Response({"ofBackendData":serializer.data}, status=200)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)
