fetch("data/info.json").then(res => res.json()).then(data => {
    // console.log(info);
    const info = data.info;
    const infoContainer = document.getElementById("info-container");
    info.forEach(item => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.innerHTML = `
            <div class="card-top">
                <img src="${item.photo ||"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJ8AAACUCAMAAAC6AgsRAAAAY1BMVEUaGhr///8AAAAXFxcGBgbf398TExMMDAwQEBDs7Oz29va9vb1gYGAqKiqPj4+np6ewsLDPz89ra2vV1dVRUVGenp4jIyO2trZlZWUxMTE/Pz9ISEiDg4OJiYmWlpbGxsZ3d3dE5pERAAAC10lEQVR4nO2azZLqIBBGoQkQ8zcm0YyJjvr+TznBO1Y5ZWJ64oVm0Wfh+lQToPtDIRiGYRiGYRiGYRiGYRiGiQSlFLXCDMqC4+c3NksDXVHlOpNSZjqvig4MtdIDBuy5dW53svZs4zGEspLPVCVQi91Q0OgJPSl1AxF8hgqqbFJvXOWKXtDA54yd45P6I1Tw8UJPyg/iCi7oOUFSvcOCnpQHQsG03yz6bfqUzG9xdWlXOD0ul28s4JGqgKjyERYQ5g7m32REftCg9KRsaARhi/TbkviptEb61SnFJWKG6bblGT1Q3MLpDnO6ODY7ihPGFrjtO27gwlL4HdB+BxK/yOsX+/cX+/5VFn3+0Yzrkd8fAgqkX0Hjp9D9C9GMBHuU356q/0uPmAJmZP2zSOKeP0RaLh+BuqSb32Kff0fBqWTtkYo2ZFNmIX8xxAnW64CIOh5ygnZ+iasYcnIFu5n8dEdfvRtgqudWcFOZhFrsjoHh9LuG+jRQR6e/MAD9V15rR51/9RCV3Q33ctQPx6F370fUMjMYB7UEwzAYlElgiYSsgzGghuact3qeNj83gyA5qxV0pwvqfeFy6sI3CiAmeoJZxUqEbaMVXLHh0E+/cA1ZQgN7bPZ3J9uH+wqtwCZXj9QiUNdgRL5CT8pcBKmgsuv0RsEg4wicV+qFSYoAHds/k/kPE1TZrtaTsi19rzBc39CT8uq7gIC/NabYePZDZ85zFH6HYlh7ttzJvRbQIALJ1+jS5yGNf3Obw+9b3Ju71+F1By/Gpct4DVSR/3h5hdc4H/3kNo/Xx7jo67e+d7nj9ftL/sP+9XmB4N/M59C91yb65b9hMfi934Tt3/Tz/Rr35g72/pipxOUNvYvwPiHZcs3w+4+6DDAC23L1fBlCz6UbzZoZqW2CJRzQNVv9l04w09umCxhhKZeb2gSNy1GDR4DqD4R2YxiGYRiGYRiGYRiGYRhm5BvoIyHtjsmsVwAAAABJRU5ErkJggg=="}" alt="${item.name}" class="card-image">
                <div class="card-info">
                    <h3 class="card-name">${item.name}</h3>
                    <p class="card-id">${item.id}</p>
                </div>
            </div>
            <p class="card-bio">${item.name}</p>
        `;
        infoContainer.appendChild(card);
    });
});
