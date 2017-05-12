# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DeptorForm
from .. import db
from ..models import Deptor

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Deptors Views

@admin.route('/deptors', methods=['GET', 'POST'])
@login_required
def list_deptors():
    """
    List all deptors
    """
    check_admin()

    deptors = Deptor.query.all()

    return render_template('admin/deptors/listdeptors.html',
                           deptors=deptors, title="Deptors")

@admin.route('/deptors/add', methods=['GET', 'POST'])
@login_required
def add_deptor():
    """
    Add a deptor to the database
    """
    check_admin()

    add_deptor = True

    form = DeptorForm()
    if form.validate_on_submit():
        deptor = Deptor(fullnames=form.fullname.data,
                        mobilenumber=form.mobileno.data,
                        nationalid=form.nationalid.data,
                        deptamount=form.deptamount.data,
                        description=form.description.data,)
        try:
            # add deptor to the database
            db.session.add(deptor)
            db.session.commit()
            flash('You have successfully added a new deptor.')
        except:
            # in case deptor name already exists
            flash('Error: deptor name already exists.')

        # redirect to deptors page
        return redirect(url_for('admin.list_deptors'))

    # load deptor template
    return render_template('admin/deptors/addeditdeptor.html', action="Add",
                           add_deptor=add_deptor, form=form,
                           title="Add Deptor")

@admin.route('/deptors/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_deptor(id):
    """
    Edit a deptor
    """
    check_admin()

    add_deptor = False

    deptor = Deptor.query.get_or_404(id)
    form = DeptorForm(obj=deptor)
    if form.validate_on_submit():
        deptor.fullnames = form.fullname.data
        deptor.mobilenumber = form.mobileno.data
        deptor.nationalid = form.nationalid.data
        deptor.deptamount = form.deptamount.data
        deptor.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the deptor.')

        # redirect to the deptors page
        return redirect(url_for('admin.list_deptors'))

    form.fullname.data = deptor.fullnames
    form.mobileno.data = deptor.mobilenumber
    form.nationalid.data = deptor.nationalid
    form.deptamount.data = deptor.deptamount
    form.description.data = deptor.description
    return render_template('admin/deptors/addeditdeptor.html', action="Edit",
                           add_deptor=add_deptor, form=form,
                           deptor=deptor, title="Edit Deptor")

@admin.route('/deptors/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_deptor(id):
    """
    Delete a deptor from the database
    """
    check_admin()

    deptor = Deptor.query.get_or_404(id)
    db.session.delete(deptor)
    db.session.commit()
    flash('You have successfully deleted a deptor.')

    # redirect to the deptors page
    return redirect(url_for('admin.list_deptors'))

    return render_template(title="Delete Deptor")
