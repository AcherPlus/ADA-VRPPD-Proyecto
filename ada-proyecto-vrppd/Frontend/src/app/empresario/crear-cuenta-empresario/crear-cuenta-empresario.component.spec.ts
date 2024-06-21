import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearCuentaEmpresarioComponent } from './crear-cuenta-empresario.component';

describe('CrearCuentaEmpresarioComponent', () => {
  let component: CrearCuentaEmpresarioComponent;
  let fixture: ComponentFixture<CrearCuentaEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CrearCuentaEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CrearCuentaEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
