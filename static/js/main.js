document.addEventListener('DOMContentLoaded', () => {
    // Select edit crime button
    document.querySelector('.edit-crime').addEventListener('click', getCrimeId);
    // Select edit suspect button
    document.querySelector('.edit-suspect').addEventListener('click', getSuspectId);
    // Select spotted eyeball
    document.querySelector('.spot-suspect').addEventListener('submit', spotSuspect);
});


const showCrimeEdit = crime_id => {
    document.querySelector(`#crime-description-${crime_id}`).style.display = 'none';
    document.querySelector(`#edit-description-${crime_id}`).style.display = 'none';
    document.querySelector(`#save-crime-${crime_id}`).style.display = 'block';
};


const showSuspectEdit = suspect_id => {
    document.querySelector(`#suspect-description-${suspect_id}`).style.display = 'none';
    document.querySelector(`#edit-description-${suspect_id}`).style.display = 'none';
    document.querySelector(`#save-suspect-${suspect_id}`).style.display = 'block';
};


const getCrimeId = crime_id => {
    const crimeId = crime_id.value;
    // Show/hide DOM elements
    showCrimeEdit(crimeId);
    // Call updateCrime function on submit
    document.querySelector(`#save-crime-${crimeId}`).addEventListener('submit', () => updateCrime(crimeId));
};


const getSuspectId = suspect_id => {
    const suspectId = suspect_id.value;
    // Show/hide DOM elements
    showSuspectEdit(suspectId);
    // Call updateCrime function on submit
    document.querySelector(`#save-suspect-${suspectId}`).addEventListener('submit', () => updateSuspect(suspectId));
};


const updateCrime = crime_id => {
    event.preventDefault();

    const crimeBody = document.querySelector(`#crime-description-${crime_id}`);
    const description = document.querySelector(`#compose-description-${crime_id}`).value;
    const crimeURL = `editcrime/${crime_id}`;
    const csrftoken = getCookie('csrftoken');
    
    const descData = {
        description
    };
    
    fetch(crimeURL, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(descData)
    })
    .then(res => res.json())
    .then(data => {
        crimeBody.innerHTML = descData.description;
        
        // Show/hide DOM elements
        document.querySelector(`#crime-description-${crime_id}`).style.display = 'block';
        document.querySelector(`#edit-description-${crime_id}`).style.display = 'block';
        document.querySelector(`#save-crime-${crime_id}`).style.display = 'none';
        
    })
    .catch(error => {
        console.log('Error', error);
    });
    return false;
};


const updateSuspect = suspect_id => {
    event.preventDefault();

    const suspectBody = document.querySelector(`#suspect-description-${suspect_id}`);
    const description = document.querySelector(`#compose-description-${suspect_id}`).value;
    const suspectURL = `editsuspect/${suspect_id}`;
    const csrftoken = getCookie('csrftoken');
    
    const descData = {
        description
    };
    
    fetch(suspectURL, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(descData)
    })
    .then(res => res.json())
    .then(data => {
        suspectBody.innerHTML = descData.description;
        
        // Show/hide DOM elements
        document.querySelector(`#suspect-description-${suspect_id}`).style.display = 'block';
        document.querySelector(`#edit-description-${suspect_id}`).style.display = 'block';
        document.querySelector(`#save-suspect-${suspect_id}`).style.display = 'none';
        
    })
    .catch(error => {
        console.log('Error', error);
    });
    return false;
};


const spotSuspect = suspect_id => {
    event.preventDefault();
    const suspectId = parseInt(suspect_id.name);
    const spotURL = `spot/${suspectId}`;
    let numSpotted = document.querySelector(`#spotted-count-${suspectId}`);
    let spottedBy = document.querySelector(`#spotted-by-${suspectId}`);
    const csrftoken = getCookie('csrftoken');
    
    fetch(spotURL, {
       method: 'PUT',
       headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    })
    .then(res => res.json())
    .then(data => {
      const spotted = data.spotted;
      const spottedArray = data.spot.map(item => `<li class="list-group-item">${item}</li>`).join(' ');
      numSpotted.innerHTML = `Spotted ${spotted} time${spotted !== 1 ? 's': ''}`; 
      spottedBy.innerHTML = 
        `Spotted by: ${spottedArray}`;
    })
    .catch(error => {
        console.log('Error', error);
    });
    return false;
};


// Cookie handler from Django docs
const getCookie = name => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
