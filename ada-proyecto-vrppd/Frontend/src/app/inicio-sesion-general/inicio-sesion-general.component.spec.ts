import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InicioSesionGeneralComponent } from './inicio-sesion-general.component';

describe('InicioSesionGeneralComponent', () => {
  let component: InicioSesionGeneralComponent;
  let fixture: ComponentFixture<InicioSesionGeneralComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InicioSesionGeneralComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InicioSesionGeneralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
