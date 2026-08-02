fetch("data/info.json").then(res => res.json()).then(data => {
    // console.log(info);
    const info = data.info;
    const infoContainer = document.getElementById("info-container");
    info.forEach(item => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.innerHTML = `
            <div class="card-top">
                <img src="${item.photo}" alt="${item.name}" class="card-image">
                <div class="card-info">
                    <h3 class="card-name">${item.name}</h3>
                    <p class="card-id">${item.id}</p>
                    <p class="card-role">${item.name}</p>
                </div>
            </div>
            <p class="card-bio">${item.name}</p>
        `;
        infoContainer.appendChild(card);
    });
});