console.log('hello world')

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')

const csrf = document.getElementById('csrfmiddlewaretoken')
  
const handleStarSelect = (size) => {
  const children = form.children
  for (let i = 0; i < children.length; i++){
    if (i <= size){
      children[i].classList.add('checked')
    } else {
      children[i].classList.remove('checked')
    }
  }
}

const handleSelect = (selection) => {
  switch(selection){
    case 'first':{
      console.log("1")
      handleStarSelect(1)
      return
    }
    case 'second':{
      handleStarSelect(2)
      return
    }
    case 'third':{
      handleStarSelect(3)
      return
    }
    case 'fourth':{
      handleStarSelect(4)
      return
    }
    case 'fifth':{
      handleStarSelect(5)
      return
    }
  }
}
if (one){
  const arr = [one, two, three, four, five]
  arr.forEach(item => item.addEventListener('mouseover', (event)=>{
    console.log(event.target)
  }))

  arr.forEach(item=> item.addEventListener('click', (event)=>{
    console.log('clicked')
  }))
}