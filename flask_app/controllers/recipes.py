from flask_app import app 
from flask import render_template, redirect, session, request  
from flask_app.models import recipe, user


@app.route('/addRecipe')
def addRecipe(): 
    if 'user_id' not in session: 
        return redirect ('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('add.html', users=user.User.getOne(data))


@app.route('/createRecipe', methods=['POST'])
def createRecipe(): 
    if 'user_id' not in session : 
        return redirect('/logout')
    if not recipe.Recipe.validateRecipe(request.form):
        return redirect('/addRecipe')
    data = {
        "name": request.form['name'],
        "description": request.form['description'], 
        "instruction": request.form['instruction'],
        "time": int(request.form['time']), 
        "dateMade": request.form['dateMade'],
        "user_id": session['user_id']
    }
    print(data)
    recipe.Recipe.save(data)
    return redirect("/dashboard")


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session: 
        return redirect('/logout')
    data = {
        "id": id
    }
    userData = {
        "id": session['user_id']
    }
    return render_template('edit.html', recipeEdit=recipe.Recipe.getOne(data), user=user.User.getOne(userData))

@app.route('/update', methods=['POST']) 
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not recipe.Recipe.validateRecipe(request.form):
        return redirect('/addRecipe')
    data = {
        "name": request.form['name'],
        "description": request.form['description'], 
        "instruction": request.form['instruction'],
        "time": (request.form['time']), 
        "dateMade": request.form['dateMade'],
        "id": request.form['id'],
    }
    recipe.Recipe.update(data)
    return redirect('/dashboard')


@app.route('/show/<int:id>')
def show(id): 
    if 'user_id' not in session: 
        return redirect('/logout')
    data = {
        'id': id
    }

    userData = {
        "id": session['user_id']
    }
    return render_template('show.html', recipe=recipe.Recipe.getOne(data), user=user.User.getOne(userData))




@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session: 
        return redirect('/logout')
    data = {
        "id":id
    }
    recipe.Recipe.delete(data)
    return redirect ('/dashboard')