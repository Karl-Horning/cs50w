document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {
        // Initialise new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        // Callback function for when request completes
        request.onload = () => {
            // Extract JSON data from request
            const data = JSON.parse(request.responseText);
            const resultsKeys = Object.keys(data.rate.results);

            // Update the result div
            // Check if the data query was successful and if the returned JSON contains data
            if(data.success && resultsKeys.length !== 0) {                
                const contents = `1 EUR is equal to ${data.rate.results[resultsKeys].val} ${currency}`;                
                document.querySelector('#result').innerHTML = contents;
            } else {
                document.querySelector('#result').innerHTML = 'There was an error';
            }
        }
        // Add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        // Send request
        request.send(data);
        return false;
    };
});