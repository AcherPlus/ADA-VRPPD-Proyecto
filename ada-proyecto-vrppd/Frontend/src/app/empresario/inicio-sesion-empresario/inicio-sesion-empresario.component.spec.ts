import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InicioSesionEmpresarioComponent } from './inicio-sesion-empresario.component';

describe('InicioSesionEmpresarioComponent', () => {
  let component: InicioSesionEmpresarioComponent;
  let fixture: ComponentFixture<InicioSesionEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InicioSesionEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InicioSesionEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
