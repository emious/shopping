src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"
const search_input=document.getElementById('test5')
var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

const results_box=document.getElementById('cities_id_one')

const new_url='/news/'

const send_search_data = (search_text) => {
    $.ajax({
        url:'get_cities_api',
        type: 'POST',
        data: {
            id: search_text,
            csrfmiddlewaretoken: csrf_token,
        },

        success: function(result) {
                    const data=result
                    if (Array.isArray(data)) {
                         results_box.innerHTML="<option> انتخاب شهر</option>"
                        data.forEach(i =>{
                            results_box.innerHTML += `
                            <option value='${i}'>${i}</option>
                            `
                        })
                    }
                    },
        error:(err) => {
            console.log('fail')
            console.log(err)
        }
      });
    };



console.log(search_input.option)
search_input.addEventListener('change', (e) =>{
    send_search_data(e.target.value)
})
