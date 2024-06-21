import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnvioResumenEmpresarioComponent } from './envio-resumen-empresario.component';

describe('EnvioResumenEmpresarioComponent', () => {
  let component: EnvioResumenEmpresarioComponent;
  let fixture: ComponentFixture<EnvioResumenEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnvioResumenEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EnvioResumenEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
