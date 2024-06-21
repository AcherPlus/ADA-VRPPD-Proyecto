import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerSeguimientoEmpresarioComponent } from './ver-seguimiento-empresario.component';

describe('VerSeguimientoEmpresarioComponent', () => {
  let component: VerSeguimientoEmpresarioComponent;
  let fixture: ComponentFixture<VerSeguimientoEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VerSeguimientoEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VerSeguimientoEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
