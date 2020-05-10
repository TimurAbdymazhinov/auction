var count = 0;

function add_photo() {
    photo_tag = document.getElementById('for_image')
    const div = document.createElement('div');

    div.className = 'form-group';
    div.id = 'div_photo' + count;
    div.innerHTML = `
        <p>Фото:</p>
        <input type="file"  class="input" name="img` + count + `" accept="image/*">
    
        <button type="button"  onclick="delete_photo(` + div.id + `)" >Удалить</button>
    `
    count += 1;
    photo_tag.appendChild(div)
}

function delete_photo(id) {
    photo_delete = id
    // photo_delete = document.getElementById(id)
    let k = photo_delete.parentNode
    k.removeChild(photo_delete)
}