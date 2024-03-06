const dateInput = document.getElementById('id_rep_date_time')

const picker = MCDatepicker.create({
  el: '#id_rep_date_time',
  theme: {
    theme_color: '#989C94'
  },
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", () => {
  picker.open()
})