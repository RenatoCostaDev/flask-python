
def get_contact_by_email(email, contatos_list):
    for contato in contatos_list:
        if contato["email"] == email:
            return contato
    return None
