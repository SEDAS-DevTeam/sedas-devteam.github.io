class CustomFooter extends HTMLElement{
    connectedCallback(){
        this.innerHTML = `
            <footer class="mt-auto bg-white text-dark py-3">
                <div class="container">
                    <div class="row">
                        <div class="col-6">
                            <p class="mb-1">© Copyright 2023, Daniel Pojhan.</p>
                            <p class="mb-0">Hosted using Github Pages</p>
                        </div>
                        <div class="col-6 my-auto text-end">
                            <a class="text-dark" href="https://github.com/SEDAS-DevTeam" target="_blank"><i class="fa-brands fa-github"></i></a>
                            <a class="text-dark" href="https://www.youtube.com/@danielpojhan6681" target="_blank"><i class="fa-brands fa-youtube"></i></a>
                        </div>
                    </div>
                </div>
            </footer>
        `
    }
}

class Container extends HTMLElement{
    connectedCallback(){
        let header_attr = this.getAttribute("head")
        let text_attr = this.getAttribute("text")
        let img_path = this.getAttribute("img-path")

        this.innerHTML = `
          <div class="bg-white text-dark rounded shadow border px-4 py-4 mt-3 container">
            <div class="row align-items-center">
                <div class="col-12 col-sm-4 text-center mb-3 mb-sm-0">
                    <img src="${img_path}" height="150" class="img-fluid">
                </div>
                <div class="col-12 col-sm-8 align-self-center" style="padding-left: 0.5rem;">
                    <h4>${header_attr}</h4>
                    <p>${text_attr}</p>
                </div>
            </div>
          </div>
        `
    }
}

class RedirBlock extends HTMLElement{
  connectedCallback(){
    let header_attr = this.getAttribute("head")
    let text_attr = this.getAttribute("text")
    let link = this.getAttribute("link")
    let icon_path = this.getAttribute("icn-path")
    let icon_text = this.getAttribute("icn-text")
    
    let has_icon_text = "true"
    if (icon_text == null) {
      icon_text = ""
      has_icon_text = "false"
    }
    
    this.classList.add("col-md-4")
    
    this.innerHTML = `
      <div class="bg-white text-dark p-4 rounded shadow border mt-4 mx-auto icon-block">
        <a href="${link}" target="_blank">
          <div class="d-flex justify-content-center align-items-center mb-3 thumbnail">
              <img src="${icon_path}" alt="${header_attr}" has-icn-text="${has_icon_text}">
              ${((has_icon_text == "true") ? `<span>${icon_text}</span>` : "")}
          </div>
        </a>
        <h5 class="text-center">${header_attr}</h5>
        <p class="text-center mb-0">${text_attr}</p>
      </div>
    `
  }
}

customElements.define("custom-footer", CustomFooter)
customElements.define("achieve-container", Container)
customElements.define("redir-block", RedirBlock)
