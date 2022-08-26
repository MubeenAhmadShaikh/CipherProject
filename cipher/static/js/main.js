let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelectorAll('.alert__close')
 
if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    console.log('clicked')
  )
}