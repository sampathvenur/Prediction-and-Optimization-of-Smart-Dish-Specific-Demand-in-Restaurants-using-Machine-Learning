import pandas as pd
from flask import Flask, request, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

df_inputs = pd.DataFrame(columns=['Week',
                                  'Center Id',
                                  'Dish Name',
                                  'Checkout Price',
                                  'Base Price',
                                  'Emailer For Promotion',
                                  'Homepage Featured'])

df_output = pd.DataFrame(columns=['Ingredient Name', 'Quantity', 'C_unit'])


Ord = pd.DataFrame(columns=['Week',
                            'Center Id',
                            'Dish Name',
                            'Checkout Price',
                            'Base Price',
                            'Emailer For Promotion',
                            'Homepage Featured',
                             'Estimated Orders'])


@app.route('/', methods=['GET', 'POST'])
def index():
    global df_output
    global df_inputs
    global Ord 
    
    model_name = 'hist_gradient_boosting'
    empty_fields = {}
    
    if request.method == 'POST':
        if 'addItem' in request.form:
            week = request.form['week']
            centerId = request.form['center_id']
            dishName = request.form['dish_name']
            checkoutPrice = request.form['checkout_price']
            basePrice = request.form['base_price']
            emailerForPromotion = request.form['email_for_promotion']
            homepageFeatured = request.form['homepage_featured']
            
            empty_fields = {}
            mod = {}
            if not week:
                empty_fields['week'] = True
            if not centerId:
                empty_fields['center_id'] = True
            if not dishName:
                empty_fields['dish_name'] = True
            if not checkoutPrice:
                empty_fields['checkout_price'] = True
            if not basePrice:
                empty_fields['base_price'] = True
            if not emailerForPromotion:
                empty_fields['email_for_promotion'] = True
            if not homepageFeatured:
                empty_fields['homepage_featured'] = True
            
            if not empty_fields:
                df_inputs.loc[len(df_inputs)] = [week,
                                                 centerId,
                                                 dishName,
                                                 checkoutPrice,
                                                 basePrice,
                                                 emailerForPromotion,
                                                 homepageFeatured]
        
        elif 'deleteItem' in request.form:
            index = int(request.form['deleteItem'])
            if 0 <= index < len(df_inputs):
                df_inputs = df_inputs.drop(index)
                
        elif 'submit' in request.form:

            
            if len(df_inputs) != 0:
                
                inData = df_inputs.merge(recipeData, left_on='Dish Name', right_on='Dish Name', how= "left")
            
                inData = inData.drop(['Dish Name'], axis = 1) 
                
                model = getModel(model_name)
                
                if model is not None:
                    orders, df_output = inputData(inData, model)
                    
                    Ord = pd.concat([df_inputs, orders], axis = 1)
                
                else:
                    print("Model is none")
                
                
                
                
    else:
        
        empty_fields = {}
    
    dropdown_options_center_id = center_id 
    dropdown_options_dish_name = dish_name 
   
    return render_template('index.html',
                           empty_fields=empty_fields,
                           dropdown_options_center_id=dropdown_options_center_id,
                           dropdown_options_dish_name=dropdown_options_dish_name,
                           df_inputs=df_inputs.iterrows(),
                           df_output=df_output.to_dict('records'),
                            Ord = Ord.to_dict('records'))


if __name__ == '__main__':
    app.run()