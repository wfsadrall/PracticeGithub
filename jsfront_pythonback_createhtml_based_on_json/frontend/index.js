fetch("http://192.168.1.5:8002")
    .then(res => res.json())
    .then(data  => {
        let body = document.getElementsByTagName('body')[0]
        for (let x = 0; x < data.length; x++){
            console.log(data[x].name)
            let template  = document.getElementById('informations')

            console.log(template)
            let clone = template.content.cloneNode(true);
            let selectH1 = clone.querySelector('h1')
            selectH1.textContent = data[x].name
            console.log(selectH1)
            
            let selectP = clone.querySelector('p')
            console.log(selectP.textContent)
            selectP.textContent = selectP.textContent.replace('{age}',data[x].age)
            let selectUL = clone.querySelector('ul')
//            console.log(template)
                        //template.querySelector
            console.log(selectUL)
            for (let i = 0; i < data[x].good_in.length; i++){
                let li = document.createElement('li')
                li.textContent = data[x].good_in[i]
                selectUL.appendChild(li)
            }

        

            body.appendChild(clone)

         
    
        }     
        let h2 = document.createElement('h2')
         //document.getElementById('hi').innerHTML = JSON.stringify(data)
         h2.textContent = JSON.stringify(data)
         body.appendChild(h2)


    })
    .catch(error => console.error(error));


//document.getElementById('things').innerHTML = data[0].name