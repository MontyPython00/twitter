const btnDeleteAll = document.querySelectorAll('#btn-delete')
let hiddenInput = document.createElement('input')
let btnConfirm = document.createElement('button')
let createForm = document.createElement('form')
createForm.method = 'POST'
btnConfirm.name = 'confirm-delete'
btnConfirm.value = 'confirm'
btnConfirm.className = 'btn-delete-detail'
btnConfirm.innerText = 'confirm'
hiddenInput.type = 'hidden'
hiddenInput.name = 'comment_id'
createForm.innerHTML += '{% csrf_token %}'

btnDeleteAll.forEach(element => {
    element.addEventListener('click', () => {
        const commentId = element.getAttribute('value')
        const comment = document.getElementById('post-remove-form-'+commentId)
        hiddenInput.value = `${commentId}`
        createForm.appendChild(hiddenInput)
        createForm.appendChild(btnConfirm)
        comment.appendChild(createForm)
    })
}, btnDeleteAll)

